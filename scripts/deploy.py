from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helper_script import get_account


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks ... 
    if network.show_active() != 'development':
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks now ...")
        mock_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000, {"from": account})
        price_feed_address = mock_aggregator.address
        print("Mocks deployment complete ... ")


    fund_me = FundMe.deploy(price_feed_address, {"from": account},publish_source=config["networks"][network.show_active()].get("verify"),)
    print(f"contract deployed at {fund_me}")

def main():
    deploy_fund_me()