class Product:
    def __init__(self, regular_price_value=None, product_name=None, campaign_price_value=None,
                 regular_price_colour=None, campaign_price_colour=None, regular_price_line_through=None,
                 product_code=None, quantity=None, short_description=None, full_description=None):
        self.product_name = product_name
        self.regular_price_value = regular_price_value
        self.campaign_price_value = campaign_price_value
        self.regular_price_colour = regular_price_colour
        self.campaign_price_colour = campaign_price_colour
        self.regular_price_line_through = regular_price_line_through
        self.product_code = product_code
        self.quantity = quantity
        self.short_description = short_description
        self.full_description = full_description

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (
            self.product_name, self.regular_price_value, self.campaign_price_value, self.regular_price_colour,
            self.campaign_price_colour, self.regular_price_line_through)

    def __eq__(self, other):
        if self.product_name == other.product_name \
                and self.regular_price_value == other.regular_price_value \
                and self.campaign_price_value == other.campaign_price_value \
                and self.regular_price_colour == other.regular_price_colour \
                and self.campaign_price_colour == other.campaign_price_colour \
                and self.regular_price_line_through == other.regular_price_line_through:
            return True
        else:
            return False
