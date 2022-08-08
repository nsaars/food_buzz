from datetime import datetime

from cart.models import AvailableCity
from home.models import TodaySpecialProduct
from shop.models import Product, ProductImage, Category
from django.contrib.auth.models import User

User.objects.create_superuser(username='admin', password='admin')

Category.objects.create(title="Breakfast", slug="breakfast", image="category/01_iyDnf2n.jpg", menu_order=1)
Category.objects.create(title="Lunch", slug="lunch", image="category/02_NbmHHDJ.jpg", menu_order=2)
Category.objects.create(title="Dinner", slug="dinner", image="category/03_ZZxcEFi_XdSboYN.jpg", menu_order=3)

Product.objects.create(category_id=1, title="Блины с курицей", slug="bliny-s-kuricej", price=3,
                       description="Блины с курицей, сыром и сливками")
Product.objects.create(category_id=1, title="Блины с сыром и помидорами", slug="bliny-s-syrom-i-pomidorami", price=2,
                       description="Блины с сыром, свежими помидорами и сливками")
Product.objects.create(category_id=2, title="Куриный суп", slug="kurinyj-sup", price=2,
                       description="Филе курицы в бульоне")
Product.objects.create(category_id=2, title="Мясной салат", slug="myasnoj-salat", price=5,
                       description="Отварное мясо, помидоры черри, салатные листья, руккола, маринованные огурчики и "
                                   "шампиньоны, яйца, красный лук, соус из песто и бальзамика")
Product.objects.create(category_id=3, title="Киш", slug="kish", price=3, description="Киш")

ProductImage.objects.create(image="product/2022/08/04/blin-s-kuric-475x317.jpg", product_id=2)
ProductImage.objects.create(image="product/2022/08/04/blin-s-syrom-i-tom-475x317.jpg", product_id=1)
ProductImage.objects.create(image="product/2022/08/04/kish-s-vit-475x317.jpg", product_id=5)
ProductImage.objects.create(image="product/2022/08/04/kish-s-kuric-475x317_84EIcoO.jpg", product_id=5)
ProductImage.objects.create(image="product/2022/08/04/kish-s-gribami-475x317_wIY7UlL.jpg", product_id=5)
ProductImage.objects.create(image="product/2022/08/04/KurinajaLapscha.jpg", product_id=3)
ProductImage.objects.create(image="product/2022/08/04/myasnoi-475x317.jpg", product_id=4)

TodaySpecialProduct.objects.create(product_id=2, date=datetime.today())
TodaySpecialProduct.objects.create(product_id=1, date=datetime.today())
TodaySpecialProduct.objects.create(product_id=4, date=datetime.today())
TodaySpecialProduct.objects.create(product_id=5, date=datetime.today())

AvailableCity.objects.create(title="Москва", shipping_price=2)
AvailableCity.objects.create(title="Париж", shipping_price=123456)
AvailableCity.objects.create(title="Ташкент", shipping_price=1)
