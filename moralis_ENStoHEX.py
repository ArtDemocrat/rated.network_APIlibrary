# this moralis api call will work as a module for the scraping code, in order to convert ENS domains to a hex address
from moralis import evm_api

def process_element(element):
    api_key = "my_API_key"

    params = {
        "domain": element
    }

    try:
        result = evm_api.resolve.resolve_ens_domain(
            api_key=api_key,
            params=params,
        )

        if 'address' in result:
            return result['address']
        else:
            return element  # Return the original element if 'address' not found

    except Exception as e:
        print(f"Error processing element '{element}': {str(e)}")
        return None
