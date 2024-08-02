
from models import db, User, Product, Order, Cart
from app import app
from datetime import datetime

with app.app_context():

    print('Start seeding...')

    print("Deleting data...")
    User.query.delete()
    Product.query.delete()
    Order.query.delete()
    Cart.query.delete()

    print("Creating users...")

    Ava = User(id="1", name="Ava", email="ava@gmail.com", password="8463456", address="address1", created_at=datetime.now())
    Tom = User(id="2", name="Tom", email="tom@gmail.com", password="8768963", address="address2", created_at=datetime.now())
    Olly = User(id="3", name="Olly", email="olly@gmail.com", password="9606590", address="address3", created_at=datetime.now())
    May = User(id="4", name="May", email="may@gmail.com", password="8763874", address="address4", created_at=datetime.now())
    Amelia = User(id="5", name="Amelia", email="amelia@gmail.com", password="4674387", address="address5", created_at=datetime.now())
    Mia = User(id="6", name="Mia", email="mia@gmail.com", password="6386658", address="address6", created_at=datetime.now())
    John = User(id="7", name="John", email="john@gmail.com", password="6986366", address="address7", created_at=datetime.now())
    Dan = User(id="8", name="Dan", email="dan@gmail.com", password="8943009", address="address8", created_at=datetime.now())
    users = [Ava,Tom,Olly,May,Amelia,Mia,John,Dan]

    db.session.add_all(users)
    db.session.commit()


    print("Creating products...")
    watch = Product(name="oraimo watch 3 Pro, 1.83", description="BT call Smart Watch", price="5999", image="https://ke.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/04/1598351/1.jpg?5040", category="watch")
    watch2 = Product(name="oraimo Watch ES 2 1.95", description="AMOLED IP68 Smart Watch", price="4500", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/05/25/OSW-810.png", category="watch")
    watch3 = Product(name="oraimo Watch Nova V 2.01", description="HD Video Watch Faces Smart Watch", price="5200", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/20/OSW-802N.png", category="watch")
    headphones = Product(name="oraimo Necklace Lite Call", description="Vibration Wireless Headphones", price="1900", image="https://cdn-img.oraimo.com/fit-in/600x600/MA/product/2024/03/19/OEB-311.png", category="headphones")
    earbuds = Product(name="oraimo Freepods pro + Hybrid ANC", description="True Wireless Earbuds", price="5500", image="https://cdn-img.oraimo.com/fit-in/600x600/MA/product/2024/05/20/OEB-E108DC.png", category="earbuds")
    powerbank = Product(name="oraimo Traveler Link 27", description="27000mAh 12W Power Bank", price="4100", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/28/opb-p5271-black.png", category="powerbank")
    headphones2 = Product(name="oraimo BoomPop 2 ENC", description="Over-Ear Wireless Headphones", price="2600", image="https://cdn-img.oraimo.com/fit-in/600x600/NG/album/ohp-610/ohp-610-black.png", category="headphones")
    watch4 = Product(name="ZL02 Smart Watch", description="H Full S Reen Sport Fitness Black", price="2690", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/37/523878/1.jpg?2248", category="smartwatch")
    phone = Product(name="Samsung Galaxy A35 5G, 6.6", description="256GB + 8GB RAM (Dual SIM), 5000mAh, Awesome Navy", price="45999", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/34/2888232/1.jpg?2068", category="phones")
    phone2 = Product(name="Oppo Reno11 F 5G", description="8GB+256GB, 64MP,5000mAh,(Dual Sim) Palm Green (2YR WRTY)", price="46999", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/59/0881742/1.jpg?1487", category="phones")
    phone3 = Product(name="Samsung Galaxy A55 5G, 6.6", description="256GB + 8GB RAM (Dual SIM), 5000mAh, Awesome Lilac", price="55499", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/70/8221332/1.jpg?8433", category="phones")
    headphones3 = Product(name="Wireless L350", description="Foldable Sports Stereo Bluetooth Headset(Black)", price="5000", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/45/2254212/1.jpg?9740", category="headphones")
    powerbank2 = Product(name="oraimo 27000 MAh", description="Travellers Portable Power Bank_Black", price="3100", image="https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/58/4494581/1.jpg?6507", category="powerbank")
    earbuds2 = Product(name="oraimo AirBuds 4 ENC", description="True Wireless Earbuds", price="2100", image="https://cdn-img.oraimo.com/fit-in/600x600/AE/product/2024/02/06/OTW-340-680-1.png", category="earbuds")
    earbuds3 = Product(name="oraimo FreePods Neo", description="ENC True Wireless Earbuds", price="2200", image="https://cdn-img.oraimo.com/fit-in/600x600/KE/product/2024/06/20/OTW-330S-black.png", category="earbuds")
    products = [watch,watch2,watch3,headphones,earbuds,powerbank, headphones2,watch4,phone,phone2,phone3,earbuds2,earbuds3]

    db.session.add_all(products)
    db.session.commit()

    print("Creating orders...")

    ord1 = Order(id="1", amount="4100", status="Pending order")
    ord2 = Order(id="2", amount="1900", status="Pending approval")
    ord3 = Order(id="3", amount="5000", status="In Transit")
    ord4 = Order(id="4", amount="5499", status="Shipping")
    ord5 = Order(id="5", amount="5200", status="Pending payment")
    ord6 = Order(id="6", amount="4100", status="Waiting to be shipped")
    ord7 = Order(id="7", amount="2100", status="Shipped to branch")
    ord8 = Order(id="8", amount="5999", status="Delivered")
    ord9 = Order(id="9", amount="2600", status="Shipping")
    ord10 = Order(id="10", amount="4500", status="Cancelled") 
    ord11 = Order(id="11", amount="4100", status="Returned")   
    orders = [ord1,ord2,ord3,ord4,ord5,ord6,ord7,ord8,ord9,ord10,ord11]

    db.session.add_all(orders)
    db.session.commit()

    #print("Cart seeding...")
    #carts = []
    #db.session.add(carts)
    #db.session.commit()

    print('Users seeded')
    print('Products seeded')
    print('Orders seeded')
    print('Cart seeded')
    print("Seeding done!")