# Elasticsearch and Kibana Tutorial

## Introduction

Elasticsearch is a powerful search and analytics engine, while Kibana is a visualization tool used to interact with Elasticsearch. Together, they form a part of the ELK Stack (Elasticsearch, Logstash, Kibana) which is commonly used for log and event data analysis.

## Prerequisites

- Docker and Docker Compose installed on your machine
- Basic knowledge of Docker commands

## Setup with Docker Compose

1. **Create a `.env` file** with the following content to store your environment variables inside the esdata directory:

    ```plaintext
    ELASTIC_PASSWORD=your_elastic_password
    ```

2. **Create a `docker-compose.yml` file** with the following content to set up Elasticsearch and Kibana:

    ```yaml
    version: '3.7'

    services:
      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:7.13.2
        container_name: elasticsearch
        environment:
          - node.name=elasticsearch
          - cluster.name=docker-cluster
          - discovery.type=single-node
          - bootstrap.memory_lock=true
          - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
          - xpack.security.enabled=true
          - ELASTIC_USERNAME=elastic
          - ELASTIC_PASSWORD=${ELASTIC_PASSWORD}
        ulimits:
          memlock:
            soft: -1
            hard: -1
        volumes:
          - esdata:/usr/share/elasticsearch/data
        ports:
          - 9200:9200
        networks:
          - elastic

      kibana:
        image: docker.elastic.co/kibana/kibana:7.13.2
        container_name: kibana
        environment:
          - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
          - ELASTICSEARCH_USERNAME=elastic
          - ELASTICSEARCH_PASSWORD=${ELASTIC_PASSWORD}
          - SERVER_NAME=kibana
        ports:
          - 5601:5601
        networks:
          - elastic
        depends_on:
          - elasticsearch

    volumes:
      esdata:
        driver: local

    networks:
      elastic:
        driver: bridge
    ```

3. **Start the services** by running:

    ```sh
    docker-compose up -d
    ```

## Accessing Kibana

- Open your browser and go to [http://localhost:5601](http://localhost:5601).
- Log in using the username `elastic` and the password you set in the `.env` file.

## Basic Elasticsearch Operations

### Indexing Data

To add documents to Elasticsearch, use the following command structure:

```sh
curl -X POST "localhost:9200/my-index-000001/_doc/1" -H 'Content-Type: application/json' -d'
{
  "field1": "value1",
  "field2": "value2"
}
'
```

### Searching Data

To search for documents in an index, use:

```sh
curl -X GET "localhost:9200/my-index-000001/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "field1": "value1"
    }
  }
}
'
```

### Deleting Data

To delete a document by ID, use:

```sh
curl -X DELETE "localhost:9200/my-index-000001/_doc/1"
```

## Visualizing Data with Kibana

### Creating Index Patterns

1. In Kibana, go to **Management > Stack Management > Index Patterns**.
2. Click **Create index pattern**.
3. Enter the index pattern that matches your Elasticsearch indices (e.g., `my-index-*`).
4. Configure the time field if applicable, then click **Create index pattern**.

### Creating Visualizations

1. In Kibana, go to **Visualize Library**.
2. Click **Create visualization**.
3. Choose the type of visualization you want to create (e.g., bar chart, line chart).
4. Select the index pattern you created.
5. Configure the visualization by adding metrics and buckets.

### Creating Dashboards

1. In Kibana, go to **Dashboard**.
2. Click **Create dashboard**.
3. Click **Add** to add visualizations to your dashboard.
4. Select the visualizations you created and arrange them as desired.
5. Save the dashboard with a meaningful name.

## Conclusion

This tutorial provides a basic setup and introduction to working with Elasticsearch and Kibana. From here, you can explore more advanced features and configurations to suit your needs. Happy exploring!
