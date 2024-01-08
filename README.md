# PaySpaceEval

## Introduction
`Payspace Eval` is a sample web-base portal created for registering and transaction of crypto-currencies between addresses. 

## How to install the project

`PaySpace Eval` is a `Django`-based application that utilizes `PostgreSql` as a support database for local tracking 
of all its activities. The project is containerized using Docker, making it easy to deploy and manage across multiple
environments. With Docker, users can run the application on their machine without the need for complex software setups.
In case you require assistance with Docker installation, please refer to the following webpage for detailed instructions.

- [Install on Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Install on Mac](https://docs.docker.com/desktop/install/mac-install/)
- [Install on Windows](https://docs.docker.com/desktop/install/windows-install/)


Please follow the instructions mentioned below to install the `PaySpace Eval`.

* To install the project, please run the following command inside your `Terminal` or `PowerShell`.

``` shell
./install.sh
```

**Note:** It is possible that the `install.sh` file is not executable. In this case, run the following command first:

```shell
chmod +x install.sh
```


## How to use `PaySpace`

In order to use `PaySpace`, you need to have pre-existing resources, such as an
`Azure Storage Container` and `Azure File Sync`. To learn how to create these resources, please follow the
instructions provided:

- [Azure Bolb Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal)
- [Azure Shae Folder](https://learn.microsoft.com/en-us/azure/storage/files/storage-how-to-use-files-portal?tabs=azure-portal)
- [Azure File Sync](https://learn.microsoft.com/en-us/azure/storage/file-sync/file-sync-deployment-guide?tabs=azure-portal%2Cproactive-portal)

Please add the requested information to the `src/settings.json` file located at:

```json
{
  "PostgreSQL": {
    "POSTGRES_HOST" : "[postgress_host]",
    "POSTGRES_DB"   : "[postgress_db_name]",
    "POSTGRES_USER" : "[postgress_user_name",
    "POSTGRES_PASSWORD" : "[postgress_password]",
    "POSTGRES_PORT" : 5432
  },
  "BlockCypher" : {
    "CHAIN" : "test3",
    "COIN"  : "btc",
    "BlockCypher_BASE_ADDRESS" : "https://api.blockcypher.com/v1/",
    "BlockCypher_Wallet_Address": "addrs",
    "BlockCypher_Transaction_Address": "txs"
  },
  "UserManagement" : {
    "known_salt" : "[salt for hashing the passwords]",
    "expires_days" : 7
  }
}
```

* To initiate the `PaySpace Eval`, utilize the following command:

```shell
./run.sh
```

**Note:** It is possible that the `run.sh` file is not executable. In this case, run the following command first:

```shell
chmod +x run.sh
```

* To access the portal pleas use the following address:

  * [http://127.0.0.1:8000](http://127.0.0.1:8000)

* To access the endpoints documentation, please follow the link provided below:
  * [http://127.0.0.1:8000/docs/redoc/](http://127.0.0.1:8000/docs/redoc/)







