class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  
  def __repr__(self):
    return '{artist}. "{title}". {year}, {medium}. {owner}, {location}.'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, owner=self.owner.name, location=self.owner.location)

class Marketplace:
  def __init__(self, listings=[]):
    self.listings = listings
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, listing):
    self.listings.remove(listing)

  def show_listings(self):
    if len(self.listings) == 0:
      print('No current listings.')
    for listing in self.listings:
      print(listing)

veneer = Marketplace()

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    dollars = "${:,.2f}".format(price)
    if (artwork.owner.name == self.name):
      new_listing = Listing(artwork, dollars, self.name)
      veneer.add_listing(new_listing)

  def buy_artwork(self, artwork):
    if (self.name == artwork.owner.name):
      print('You already own this item.')
      return
    for listing in veneer.listings:
      if(listing.art == artwork):
        art_listing = listing
        artwork.owner = self
        print('{new_owner} bought {title} from {previous_owner} for {price}.'.format(new_owner=self.name, title=artwork.title, previous_owner=art_listing.seller, price=listing.price))
        veneer.remove_listing(art_listing)
    print('That item is not for sale.')


edytta = Client('Edytta Halpirt', 'Private Collection', False)

moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas','1910', edytta)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  
  def __repr__(self):
    return '{art}: {price}'.format(art=self.art.title, price=self.price)

edytta.sell_artwork(girl_with_mandolin, 6000000)

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)
