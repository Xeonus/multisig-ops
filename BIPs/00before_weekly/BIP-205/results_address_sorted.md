| deployment                                 | chain   | function                                                                                                          | role                                                               | target                         | target_address                             |
|:-------------------------------------------|:--------|:------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|:-------------------------------|:-------------------------------------------|
| 20221122-composable-stable-pool-v2         | gnosis  | setSwapFeePercentage(uint256)                                                                                     | 0x60b21b2ae5a82434b74afd79abbbafb941197b06237922de3a54d36aaa9c4ea2 | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20221122-composable-stable-pool-v2         | gnosis  | startAmplificationParameterUpdate(uint256,uint256)                                                                | 0xd82b3ab66c70adebd687f4d69dae8b0abd33cacede07deb0c948dc2383f4aeb7 | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20221122-composable-stable-pool-v2         | gnosis  | stopAmplificationParameterUpdate()                                                                                | 0x8ab1e42805feb8214d075b216e36ee38c5f3064d5c2ada1d99aa9f63367a029d | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20221207-aave-rebalanced-linear-pool-v3    | gnosis  | setSwapFeePercentage(uint256)                                                                                     | 0x528c3020f2bd77511812b0aacb3cb91170124524cfdf0d4941db79d4ebf6ff72 | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20220527-child-chain-gauge-token-adder     | gnosis  | addTokenToGauge(address,address,address)                                                                          | 0x1ff8dca7a9af725b8fde69703b657ae58c04e9a7153ef1025379deb0dda4f926 | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20220517-protocol-fee-withdrawer           | gnosis  | withdrawCollectedFees(address[],uint256[],address)                                                                | 0xf6c9a5b5acca77f76aed5abd6f810c52c3ff5f4a8a40ee9e1bc09f85795e73da | lm                             | 0x14969B55a675d13a1700F71A37511bc22D90155a |
| 20220725-protocol-fee-percentages-provider | gnosis  | setFeeTypePercentage(uint256,uint256)                                                                             | 0x77b2549a67e235e7bd37726ed4ebd404701323182a0028ea067bb8337e6e15a3 | dao                            | 0x2a5AEcE0bb9EfFD7608213AE1745873385515c18 |
| 20210418-vault                             | gnosis  | setFlashLoanFeePercentage(uint256)                                                                                | 0xbe2a180d5cc5d803a8eec4cea569989fc1c593d7eeadd1f262f360a68b0e842e | ProtocolFeePercentagesProvider | 0x41B953164995c11C81DA73D212ED8Af25741b7Ac |
| 20210418-vault                             | gnosis  | setSwapFeePercentage(uint256)                                                                                     | 0xb28b769768735d011b267f781c3be90bce51d5059ba015bc7a28b3e882fb2083 | ProtocolFeePercentagesProvider | 0x41B953164995c11C81DA73D212ED8Af25741b7Ac |
| 20220413-child-chain-gauge-factory         | gnosis  | notify_reward_amount(address)                                                                                     | 0xf139842955587e7816c90b6d72792f2b7e6014d560464517094450df28164bc8 | blabs_ops                      | 0x955556b002d05c7B31a9394c10897c1DA19eAEab |
| 20221123-pool-recovery-helper              | gnosis  | addPoolFactory(address)                                                                                           | 0x27f2737d0304362f4d515085adcfa1319a27436bb556d75e8ce5216c8ad601be | blabs_ops                      | 0x955556b002d05c7B31a9394c10897c1DA19eAEab |
| 20221123-pool-recovery-helper              | gnosis  | removePoolFactory(address)                                                                                        | 0xf73432698cd2e092161276906856b882c56056a85b0a0792733cc87cc6d49e57 | blabs_ops                      | 0x955556b002d05c7B31a9394c10897c1DA19eAEab |
| 20230206-weighted-pool-v3                  | gnosis  | enableRecoveryMode()                                                                                              | 0x2e31b466b15801536da90012c6e9916b3e0587c2d0b7c63328971c531b6ccf87 | PoolRecoveryHelper             | 0xc3ccacE87f6d3A81724075ADcb5ddd85a8A1bB68 |
| 20230206-composable-stable-pool-v3         | gnosis  | enableRecoveryMode()                                                                                              | 0xd6f4df0a512a29fa4cf2fcfbe4a0b5ea1266a4bbb1ab6fb5761205dbb038441f | PoolRecoveryHelper             | 0xc3ccacE87f6d3A81724075ADcb5ddd85a8A1bB68 |
| 20221122-composable-stable-pool-v2         | gnosis  | enableRecoveryMode()                                                                                              | 0x793ca26aa62caae6b2fb946bce982e9d0448354abd818cabb58abd0d04a3ef03 | PoolRecoveryHelper             | 0xc3ccacE87f6d3A81724075ADcb5ddd85a8A1bB68 |
| 20221207-aave-rebalanced-linear-pool-v3    | gnosis  | enableRecoveryMode()                                                                                              | 0x2b9e0eea2297118ae92c9c5b6b9ca813c821186c7eb196bd9893a4113354ec4e | PoolRecoveryHelper             | 0xc3ccacE87f6d3A81724075ADcb5ddd85a8A1bB68 |
| 20230206-aave-rebalanced-linear-pool-v4    | gnosis  | enableRecoveryMode()                                                                                              | 0x55183eaafc9e607c22ca713ce26b115fe0e7e47216af41fcec2f0fff0d6f622a | PoolRecoveryHelper             | 0xc3ccacE87f6d3A81724075ADcb5ddd85a8A1bB68 |
| 20220609-stable-pool-v2                    | gnosis  | disable()                                                                                                         | 0x06efe7e891755c060de5033e398e2d4d9f1bc713591717209ef84b7e021bd154 | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20221122-composable-stable-pool-v2         | gnosis  | pause()                                                                                                           | 0x21e53d020b912764bb3a437d64ccad86ad4b36334ab4933c92b4f7e20ec74c34 | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20221207-aave-rebalanced-linear-pool-v3    | gnosis  | disable()                                                                                                         | 0x12068567376f5214f735cd6e477a885e135c8964f6771112086ce1fda7cc475d | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20221207-aave-rebalanced-linear-pool-v3    | gnosis  | pause()                                                                                                           | 0xd919e97356fc5c0cb30e2fdb110ca94a297b955b06db82ee8d9d603c7f9d1989 | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20230206-aave-rebalanced-linear-pool-v4    | gnosis  | pause()                                                                                                           | 0x9fca6ce6b2733f09e22be866cbbfc8b9b4b6822e7ff1e1c9b5c10895e2bbb6b0 | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20210418-vault                             | gnosis  | setPaused(bool)                                                                                                   | 0xb5593fe09464f360ecf835d5b9319ce69900ae1b29d13844b73c250b1f5f92fb | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20220517-protocol-fee-withdrawer           | gnosis  | denylistToken(address)                                                                                            | 0x6843b94f991c5dbdf5c0bd1ce79ce0de10b8e72ed8b70dbe019e3eda4079802a | emergency                      | 0xd6110A7756080a4e3BCF4e7EBBCA8E8aDFBC9962 |
| 20210418-vault                             | gnosis  | withdrawCollectedFees(address[],uint256[],address)                                                                | 0xb2b6e48fa160a7c887d9d7a68b6a9bb9d47d4953d33e07f3a39e175d75e97796 | ProtocolFeesWithdrawer         | 0xdAE7e32ADc5d490a43cCba1f0c736033F2b4eFca |
| 20210418-vault                             | gnosis  | batchSwap(uint8,(bytes32,uint256,uint256,uint256,bytes)[],address[],(address,bool,address,bool),int256[],uint256) | 0x1282ab709b2b70070f829c46bc36f76b32ad4989fecb2fcb09a1b3ce00bbfc30 | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |
| 20210418-vault                             | gnosis  | exitPool(bytes32,address,address,(address[],uint256[],bytes,bool))                                                | 0xc149e88b59429ded7f601ab52ecd62331cac006ae07c16543439ed138dcb8d34 | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |
| 20210418-vault                             | gnosis  | joinPool(bytes32,address,address,(address[],uint256[],bytes,bool))                                                | 0x78ad1b68d148c070372f8643c4648efbb63c6a8a338f3c24714868e791367653 | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |
| 20210418-vault                             | gnosis  | manageUserBalance((uint8,address,uint256,address,address)[])                                                      | 0xeba777d811cd36c06d540d7ff2ed18ed042fd67bbf7c9afcf88c818c7ee6b498 | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |
| 20210418-vault                             | gnosis  | setRelayerApproval(address,address,bool)                                                                          | 0x0014a06d322ff07fcc02b12f93eb77bb76e28cdee4fc0670b9dec98d24bbfec8 | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |
| 20210418-vault                             | gnosis  | swap((bytes32,uint8,address,address,uint256,bytes),(address,bool,address,bool),uint256,uint256)                   | 0x7b8a1d293670124924a0f532213753b89db10bde737249d4540e9a03657d1aff | BalancerRelayer                | 0xeF606F58A4FD0fCcb066c6203d0994694d3eB2D3 |