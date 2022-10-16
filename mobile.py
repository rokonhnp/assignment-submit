import random

mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}
#  Your Code Starts from here

for mobiles in mobile_data['data']:
    mobile_name = mobiles.get('name')
    mobile_price = mobiles.get('price')
    mobile_made_in = mobiles.get('made')
    bdt_price = int(float(mobile_price)) * int(mobile_data['exchnage_rate'])

    template = [f'Our latest mobile {mobile_name} is made in {mobile_made_in}. The price is {mobile_price} USD which is almost equal to {bdt_price} BDT.',
                f'In 2022 new mobile released {mobile_name} is made in {mobile_made_in}. The price is {mobile_price} USD which is almost equal to {bdt_price} BDT.',
                f'{mobile_name} is made in {mobile_made_in}. The price is {mobile_price} USD which is almost equal to {bdt_price} BDT.'
                ]

    print(random.choice(template))

