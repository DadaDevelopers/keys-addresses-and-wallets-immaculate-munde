from bitcoinlib.keys import HDKey

# Generate a master key
master_key = HDKey()

print("Master Key (xprv):", master_key.wif())
print("Master Public Key (xpub):", master_key.public_master())

# Generate child keys
legacy = master_key.subkey_for_path("m/44'/0'/0'/0/0")
bech32 = master_key.subkey_for_path("m/84'/0'/0'/0/0")
bech32m = master_key.subkey_for_path("m/86'/0'/0'/0/0")

print("\nLegacy Address:", legacy.address())
print("Bech32 Address:", bech32.address())
print("Bech32m Address:", bech32m.address())
