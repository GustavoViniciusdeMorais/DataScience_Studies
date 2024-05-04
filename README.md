# Apache Airflow

- [DAGs](./dags.md)

1. **Update Package Lists**: Start by updating the package lists for upgrades and new package installations.

```bash
sudo apt update
```

2. **Install Dependencies**: Apache Airflow has several dependencies. Install them using the following command:

```bash
sudo apt install -y python3 python3-pip python3-venv libmysqlclient-dev libssl-dev libkrb5-dev krb5-user libsasl2-dev libldap2-dev libpq-dev libffi-dev
```

3. **Install Airflow**: You can install Apache Airflow using pip, the Python package installer.

```bash
pip3 install apache-airflow
```

4. **Initialize the Airflow Database**: After installing Airflow, initialize the database where Airflow will store its metadata.

```bash
airflow db init
```

5. **Start the Web Server**: Start the Airflow web server, which provides the user interface for interacting with Airflow.

```bash
airflow webserver -D --port 8080
```

6. **Start the Scheduler**: Start the Airflow scheduler, which orchestrates the execution of tasks defined in your workflows.

```bash
airflow scheduler -D
```

7. **Access Airflow Web Interface**: Open your web browser and navigate to `http://localhost:8080` (or replace `localhost` with the IP address of your server if accessing remotely). You should see the Airflow web interface, where you can manage and monitor your workflows.

### Config user
```sh
airflow users create \
          --username admin \
          --firstname FIRST_NAME \
          --lastname LAST_NAME \
          --role Admin \
          --email admin@example.org
```
