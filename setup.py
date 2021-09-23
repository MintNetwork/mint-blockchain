from setuptools import setup

dependencies = [
    "blspy==1.0.6",  # Signature library
    "chiavdf==1.0.3",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.11",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.9",  # Binary data management library
    "colorama==0.4.4",  # Colorizes terminal output
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "fasteners==0.16.3",  # For interprocess file locking
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the mint processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
    "watchdog==2.1.3",  # Filesystem event watching - watches keyring.yaml
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="mint-blockchain",
    description="Mint blockchain full node, farmer, timelord, and wallet.",
    url="https://mintnet.work/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="mint blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "mint",
        "mint.cmds",
        "mint.clvm",
        "mint.consensus",
        "mint.daemon",
        "mint.full_node",
        "mint.timelord",
        "mint.farmer",
        "mint.harvester",
        "mint.introducer",
        "mint.plotting",
        "mint.pools",
        "mint.protocols",
        "mint.rpc",
        "mint.server",
        "mint.simulator",
        "mint.types.blockchain_format",
        "mint.types",
        "mint.util",
        "mint.wallet",
        "mint.wallet.puzzles",
        "mint.wallet.rl_wallet",
        "mint.wallet.cc_wallet",
        "mint.wallet.did_wallet",
        "mint.wallet.settings",
        "mint.wallet.trading",
        "mint.wallet.util",
        "mint.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "mint = mint.cmds.mint:main",
            "mint_wallet = mint.server.start_wallet:main",
            "mint_full_node = mint.server.start_full_node:main",
            "mint_harvester = mint.server.start_harvester:main",
            "mint_farmer = mint.server.start_farmer:main",
            "mint_introducer = mint.server.start_introducer:main",
            "mint_timelord = mint.server.start_timelord:main",
            "mint_timelord_launcher = mint.timelord.timelord_launcher:main",
            "mint_full_node_simulator = mint.simulator.start_simulator:main",
        ]
    },
    package_data={
        "mint": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp", "py.typed"],
        "mint.util": ["initial-*.yaml", "english.txt"],
        "mint.ssl": ["mint_ca.crt", "mint_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
