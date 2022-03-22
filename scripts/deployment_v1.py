from brownie import FlashloanV1, accounts

AAVE_LENDING_POOL_ADDRESS_PROVIDER = "0x766C6A21d1750deCFe52601aB5b0c38feCb14073"


def main():
    """
    Deploy a `FlashloanV1` contract from `accounts[0]`.
    """

    acct = accounts.load()  # add your keystore ID as an argument to this call

    flashloan = FlashloanV1.deploy(AAVE_LENDING_POOL_ADDRESS_PROVIDER, {"from": acct})
    return flashloan
