from pages.base_page import Page
from pages.product_page import Product
from pages.top_banner import TopBanner
from pages.login_form import LoginForm
from pages.latest_products_on_sale import LatestSale
from pages.quick_view import QuickView
from pages.shopping_cart import ShoppingCart
from pages.wishlist_page import WishList
from pages.top_menu_bar import TopMenu
from pages.browse_our_categories import BrowseCategories
from pages.categories_page import Category


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.product_page = Product(self.driver)
        self.top_banner = TopBanner(self.driver)
        self.login_form = LoginForm(self.driver)
        self.latest_sale = LatestSale(self.driver)
        self.quick_view = QuickView(self.driver)
        self.shopping_cart = ShoppingCart(self.driver)
        self.wish_list = WishList(self.driver)
        self.top_menu = TopMenu(self.driver)
        self.browse_our_categories = BrowseCategories(self.driver)
        self.category = Category(self.driver)
