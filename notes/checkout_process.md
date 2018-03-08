#Checkout process

1. Cart -> Checkout View
    ?
    - Login/Register or Enter an email (as Guest)
    - Shipping Address
    - Billing Info
        -Billing Address
        - Credit Card / Payment

2. Billing App/Component
    - Billing Profile
        - User or Email (Guest Email)
        - Generate payment processor token

3. Orders / Invoice Component
    - Connectiong the billig profile
    - shipping / billing address
    - cart
    - Status -- shipped? Cancelled?

backup fixtures
python manage.py dumpdata products --format json --indent 4 > products/fixtures/products.json
python manage.py loaddata products/fixtures/products.json

