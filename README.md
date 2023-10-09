# Rated.network Performance Metrics Access Library
This repository contains a library of python scripts to:
1) Scrape the https://rocketscan.io/nodes to download all 3000+ Rocketpool node operator addresses
2) Convert all ENS domains to hex addresses
3) Run all of Rocketpool's node operator set through rated.network's validator staking performance metrics API

Current Status: **Cannot run the Rocketpool node operator addresses through rated.network's API, since the cURL endpoint requires validator indexes or public keys, while the data scraped from rocketscan.io returns node operator addresses.**

### Library Scripts for the steps above

- [Rocketpool Node Operator Address Scraping](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/RPNodeOperatorScraping.py) (**AVAILABLE**)
- [Rocketpool Node Operator ENS-to-Hex Mapping & Conversion](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/moralis_ENStoHEX.py) - required as a module for the scraping code "RPNodeOperatorScraping.py" above (**AVAILABLE**)
- [Single Validator Performance Pull](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/SingleValidatorPerformance.py) (**AVAILABLE**)
- [Direct rocketscan.io cURL](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/rocketscan_allData) - pulls RP minipool adress, pubkey, index, status (**Available**)
- Operator-level Metadata (**WIP**)
- Operator-level Summary (**WIP**)
- Network operator-level effectiveness percentile ranks (**WIP**)
- Operator-level effectiveness (by week, since dd.mm.yyyy) (**WIP**)
- Individual validator effectiveness (by validator, for n validators 0 to n) (**WIP**)
