# Rated.network API Access Library
This repository contains a library of cURL API scripts to access rated.network's validator-, operator-, and entity-level staking performance metrics. All scripts are in the form of Python commands which contain cURL requests that produces a JSON object that saved as CSVs.

### Library Scripts

- [Single Validator Performance Pull](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/SingleValidatorPerformance.py) (**AVAILABLE**)
- [Rocketpool Node Operator Address Scraping](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/RPNodeOperatorScraping.py) (**AVAILABLE**)
- [Rocketpool Node Operator ENS-to-Hex Mapping & Conversion](https://github.com/ArtDemocrat/rated.network_APIlibrary/blob/main/moralis_ENStoHEX.py) (Required as a module for the scraping code "RPNodeOperatorScraping.py" above) (**AVAILABLE**)
- Operator-level Metadata (**WIP**)
- Operator-level Summary (**WIP**)
- Network operator-level effectiveness percentile ranks (**WIP**)
- Operator-level effectiveness (by week, since dd.mm.yyyy) (**WIP**)
- Individual validator effectiveness (by validator, for n validators 0 to n) (**WIP**)
