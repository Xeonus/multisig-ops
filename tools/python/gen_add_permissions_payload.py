import json
import requests
from dotmap import DotMap
from helpers.addresses import get_registry_by_chain_id, flat_callers_by_chain
import pandas as pd
from datetime import date
from web3 import Web3
import os


today = str(date.today())
debug = False

###TODO: The below settings must be set before running the script
INFURA_KEY = os.getenv('WEB3_INFURA_PROJECT_ID')
BALANCER_DEPLOYMENTS_DIR = "../../../balancer-v2-monorepo/pkg/deployments"
BALANCER_DEPLOYMENTS_URL = "https://raw.githubusercontent.com/balancer-labs/balancer-v2-monorepo/master/pkg/deployments"

ALL_CHAINS_MAP = {
        "mainnet": 1,
        "polygon": 137,
        "arbitrum": 42161,
        "optimism": 10,
        "gnosis": 100
}

def load_input_data(input_json_file):
    with open(input_json_file, "r") as f:
        data = json.load(f)
        return data





def build_action_ids_map(input_data):
    action_ids_map = {}
    for chain in ALL_CHAINS_MAP:
        action_ids_map[chain] = {}
    for change in input_data:
        for chain_name, chain_id in change["chain_map"].items():
            callers_map = DotMap(flat_callers_by_chain(chain_name))
            result = requests.get(f"{BALANCER_DEPLOYMENTS_URL}/action-ids/{chain_name}/action-ids.json").json()
            for deployment in change["deployments"]:
                action_ids_map[chain_name][deployment] = {}
                for contract, data in result[deployment].items():
                    #action_ids_map[deployment][contract]
                    for function, action_id in data["actionIds"].items():
                        if function in change["function_caller_map"].keys():
                            ## we could get a single string caller tag or a list of caller tags
                            fxcallers = change["function_caller_map"][function]
                            if isinstance(fxcallers, str):
                                fxcallers = [fxcallers]
                            for caller in fxcallers:
                                if caller not in callers_map.keys():
                                    print (f"caller:{caller}, function: {function}")
                                action_ids_map[chain_name][deployment][function] = [action_id, caller]
    return action_ids_map


def generate_change_list(actions_id_map, input_data, ignore_already_set=True):
    changes = []
    for chain, deployments in actions_id_map.items():
        registry = get_registry_by_chain_id(ALL_CHAINS_MAP[chain])
        # Build a list of callers out of the multisigs and the other balancer addresses
        callers = registry.balancer.multisigs
        for name, value in registry.balancer.items():
            assert name not in callers.keys()
            if type(value) == str:
                callers[name] = value
        for deployment, functions in deployments.items():
            for function, action_id_and_caller_list in functions.items():
                action_id = action_id_and_caller_list[0]
                caller = action_id_and_caller_list[1]
                assert type(callers[caller]) is str, f"caller {caller} has non-str target.  Does this name exist in the registry for this chain under balancer or balancer.mutlisigs?"
                if function == "setSwapFeePercentage(uint256)" and chain == "mainnet":
                    target_address=registry.balancer.gauntletFeeSetter
                    target = "gauntletFeeSetter"
                elif caller == "poolRecoveryHelper":
                    target_address = registry.balancer.poolRecoveryHelper
                    target = caller
                else:
                    target_address=callers[caller]
                    target = caller
                #w3 = Web3(Web3.HTTPProvider(f"https://{chain}.infura.io/v3/{INFURA_KEY}"))
                w3 = Web3(Web3.HTTPProvider(f"https://rpc.gnosischain.com"))

                authorizer = w3.eth.contract(address="0xA331D84eC860Bf466b4CdCcFb4aC09a1B43F3aE6", abi=json.load(open("./abis/Authorizer.json")))
                role_members = authorizer.functions.getRoleMemberCount(action_id).call()
                if  role_members> 0:
                    if role_members == 1:
                        only_member = authorizer.functions.getRoleMember(action_id, 0).call()
                        if only_member == target_address:
                            print(f"{deployment}/{function} already has the proper owner set, skipping")
                            if ignore_already_set:
                                continue
                    else:
                        print(f"WARNING: the following has {role_members} members already: {deployment}{function}{action_id}")
                        if ignore_already_set:
                            assert(False, "unexpected permissions found")
                changes.append({
                    "deployment": deployment,
                    "chain": chain,
                    "function": function,
                    "role": action_id,
                    "target": target,
                    "target_address": target_address
                })
    return changes


def print_change_list(change_list, output_dir, filename_root=today):
    df = pd.DataFrame(change_list)
    chain_address_sorted = df.sort_values(by=["chain", "target_address"])
    chain_deployment_sorted = df.sort_values(by=["chain", "deployment", "function"])
    print(df.to_markdown(index=False))
    if output_dir:
        with open(f"{output_dir}/{filename_root}_address_sorted.md", "w") as f:
            chain_address_sorted.to_markdown(index=False, buf=f)
        with open(f"{output_dir}/{filename_root}_deployment_sorted.md", "w") as f:
            chain_deployment_sorted.to_markdown(index=False, buf=f)

def save_command_description_table(change_list, output_dir, filename_root=today):
    referenced_calls = []
    functions=[]
    descriptions=[]
    with open(f"{output_dir}/func_desc_by_name.json", "r") as f:
        func_desc_by_name = json.load(f)
    for change in change_list:
        function = change["function"]
        if function not in referenced_calls:
            if function not in functions:
                functions.append(function)
                try:
                    descriptions.append(func_desc_by_name[function])
                except:
                    descriptions.append("dscription not found in map")
    df = pd.DataFrame({
        "function": functions,
        "description": descriptions
    })
    with open(f"{output_dir}/{filename_root}_function_descriptions.md", "w") as f:
        df.to_markdown(buf=f, index=False)


def save_txbuilder_json(change_list, output_dir, filename_root=today):
    df = pd.DataFrame(change_list)
    chains=[]
    for change in change_list:
        if change["chain"] not in chains:
            chains.append(change["chain"])

    for chain_name in chains:
        chain_id = ALL_CHAINS_MAP[chain_name]
        r = get_registry_by_chain_id(chain_id)
        with open("tx_builder_templates/authorizor_grant_roles.json", "r") as f:
            data = DotMap(json.load(f))

        # Set global data
        data.chainId = chain_id
        data.meta.createFromSafeAddress = r.balancer.multisigs.dao

        # Group roles on this chain by target address
        action_ids_by_address = {}
        for change in change_list:
            if change["chain"] != chain_name:
                continue
            if change["target_address"] not in action_ids_by_address:
                action_ids_by_address[change["target_address"]] = []
            action_ids_by_address[change["target_address"]].append(change["role"])

        # Build transaction list
        transactions = []
        tx_template = data.transactions[0]
        for address,actions in action_ids_by_address.items():
            transaction = DotMap(tx_template)
            transaction.to = r.balancer.Authorizer
            # TX builder wants lists in a string, addresses unquoted
            transaction.contractInputsValues.roles = str(actions).replace("'","")
            transaction.contractInputsValues.account = address
            transactions.append(dict(transaction))
        # Inject transaction list
        data.transactions = transactions
        # Save tx builder json
        with open(f"{output_dir}/{filename_root}_{chain_name}.json", "w") as f:
            json.dump(dict(data), f)

def main(output_dir="../../BIPs/00batched/authorizer", input_file=f"../../BIPs/00batched/authorizer/{today}.json"):
    input_data = load_input_data(input_file)
    action_ids_map = build_action_ids_map(input_data)
    change_list = generate_change_list(action_ids_map, input_data, ignore_already_set=True)
    print(change_list)
    print_change_list(
        change_list=change_list,
        output_dir=output_dir
    )
    save_command_description_table(change_list=change_list, output_dir=output_dir)
    save_txbuilder_json(change_list=change_list,output_dir=output_dir)


if __name__ == "__main__":
    main()