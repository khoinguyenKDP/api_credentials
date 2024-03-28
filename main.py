from woocommerce import API

# WooCommerce API Credentials
url = 'https://azbookland.com'
consumer_key = 'ck_002a5657c51b225d9155f6fe2c6d7fd056fd6ec7'
consumer_secret = 'cs_be573bcf80f39fe015d5165e7fcc2aac60472075'

# Initialize WooCommerce API client
wcapi = API(
    url=url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    version="wc/v3"
)

# Create a new product
data = {
    "name": "Premium Quality",
    "type": "simple",
    "regular_price": "21.99",
    "description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo.",
    "short_description": "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
    "categories": [
        {
            "id": 9
        },
        {
            "id": 14
        }
    ],
    "meta_data": [
        {
            "key": "_knawatfibu_url",
            "value": {
                "img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl_1_4ZR9QmhVjCvuUtDEZ3t1Af7uW6wzFug&usqp=CAU",
                "width": 350,
                "height": 350
            }
        },
        {
            "key": "_knawatfibu_wcgallary",
            "value": [
                {"url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRl_1_4ZR9QmhVjCvuUtDEZ3t1Af7uW6wzFug&usqp=CAU"},
            ]
        }
    ]
}

# Make POST request to create the product
response = wcapi.post("products", data).json()
print(response)
