# Backend Challenge script

Simple Python command line interface to get information about the price of the provided symbol.


## Create docker image

To create the docker image, you can simpli run

```bash
docker build -t <image_name> .
```

## Run container

```
docker run -it <image_name> 
```

## Usage

You will asked to insert a symbol and then a number.
The script retrieve data on binance and print out every time the price goes above the provided input number.