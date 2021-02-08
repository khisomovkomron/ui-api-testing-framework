
API_HOSTS = {
    "test": "http://localhost:10004/wp-json/wc/v3/",
    "dev": "",
    "prod": ""

}

WOO_API_HOSTS = {
    "test": "http://localhost:10004/",
    "dev": "",
    "prod": ""

}

DB_HOST = {
    'machine1': {
        "test": {"host": "localhost",
                 "database": "threekstore",
                 "table_prefix": "wp_",
                 "socket": None,
                 "port": 10005
                 },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "wp398",
            "table_prefix": "wp2p_",
            "socket": None,
            "port": 10005
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
    },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "",
                 "port": 10005
                 },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
    }
}