class Card:
    def __init__(self, data):
        self._data = data

    def data(self):
        """Return a dictonary with all the card data in it"""
        return self._data

    def overview(self):
        """Return a formatted output with all critical details"""
        output = f'{self.name()} - {self.set_code()}'
        if self._data["mana_cost"] != "":
            output += f'- {self._data["mana_cost"]}'
        output += f'\n{self._data["type_line"]}\n{self._data["oracle_text"]}'
        if 'power' in self._data:
            output += f'\n{self._data["power"]}/{self._data["toughness"]}'
        return output

# Data Retrieval // Gameplay Fields

    def all_parts(self):
        if "all_parts" in self._data.keys():
            return self._data["all_parts"]
        else:
            raise LookupError('Card has no value "all_parts"')
        
    def card_faces(self):
        if "card_faces" in self._data.keys():
            return self._data["card_faces"]
        else:
            raise LookupError('Card has no value "card_faces"')
        
    def cmc(self):
        if "cmc" in self._data.keys():
            return self._data["cmc"]
        else:
            raise LookupError('Card has no value "cmc"')
        
    def color_identity(self):
        if "color_identity" in self._data.keys():
            return self._data["color_identity"]
        else:
            raise LookupError('Card has no value "color_identity"')
        
    def color_indicator(self):
        if "color_indicator" in self._data.keys():
            return self._data["color_indicator"]
        else:
            raise LookupError('Card has no value "color_indicator"')
        
    def colors(self):
        if "colors" in self._data.keys():
            return self._data["colors"]
        else:
            raise LookupError('Card has no value "colors"')
        
    def edhrec_rank(self):
        if "edhrec_rank" in self._data.keys():
            return self._data["edhrec_rank"]
        else:
            raise LookupError('Card has no value "edhrec_rank"')
        
    def hand_modifier(self):
        if "hand_modifier" in self._data.keys():
            return self._data["hand_modifier"]
        else:
            raise LookupError('Card has no value "hand_modifier"')
        
    def keywords(self):
        if "keywords" in self._data.keys():
            return self._data["keywords"]
        else:
            raise LookupError('Card has no value "keywords"')
        
    def layout(self):
        if "layout" in self._data.keys():
            return self._data["layout"]
        else:
            raise LookupError('Card has no value "layout"')
        
    def legalities(self):
        if "legalities" in self._data.keys():
            return self._data["legalities"]
        else:
            raise LookupError('Card has no value "legalities"')
        
    def life_modifier(self):
        if "life_modifier" in self._data.keys():
            return self._data["life_modifier"]
        else:
            raise LookupError('Card has no value "life_modifier"')
        
    def loyalty(self):
        if "name" in self._data.keys():
            return self._data["loyalty"]
        else:
            raise LookupError('Card has no value "loyalty"')
        
    def mana_cost(self):
        if "mana_cost" in self._data.keys():
            return self._data["mana_cost"]
        else:
            raise LookupError('Card has no value "mana_cost"')
        
    def name(self):
        if "name" in self._data.keys():
            return self._data["name"]
        else:
            raise LookupError('Card has no value "name"')
        
    def oracle_text(self):
        if "oracle_text" in self._data.keys():
            return self._data["oracle_text"]
        else:
            raise LookupError('Card has no value "oracle_text"')
        
    def oversized(self):
        if "oversized" in self._data.keys():
            return self._data["oversized"]
        else:
            raise LookupError('Card has no value "oversized"')
        
    def penny_rank(self):
        if "penny_rank" in self._data.keys():
            return self._data["penny_rank"]
        else:
            raise LookupError('Card has no value "penny_rank"')
        
    def power(self):
        if "power" in self._data.keys():
            return self._data["power"]
        else:
            raise LookupError('Card has no value "power"')
        
    def produced_mana(self):
        if "produced_mana" in self._data.keys():
            return self._data["produced_mana"]
        else:
            raise LookupError('Card has no value "produced_mana"')
        
    def reserved(self):
        if "reserved" in self._data.keys():
            return self._data["reserved"]
        else:
            raise LookupError('Card has no value "reserved"')
        
    def toughness(self):
        if "toughness" in self._data.keys():
            return self._data["toughness"]
        else:
            raise LookupError('Card has no value "toughness"')
        
    def type_line(self):
        if "type_line" in self._data.keys():
            return self._data["type_line"]
        else:
            raise LookupError('Card has no value "type_line"')
        
# Data Retrieval // Print Fields
    def artist(self):
        if "artist" in self._data.keys():
            return self._data["artist"]
        else:
            raise LookupError('Card has no value "artist"')

    def attraction_lights(self):
        if "attraction_lights" in self._data.keys():
            return self._data["attraction_lights"]
        else:
            raise LookupError('Card has no value "attraction_lights"')

    def booster(self):
        if "booster" in self._data.keys():
            return self._data["booster"]
        else:
            raise LookupError('Card has no value "booster"')

    def border_color(self):
        if "border_color" in self._data.keys():
            return self._data["border_color"]
        else:
            raise LookupError('Card has no value "border_color"')
    
    def card_back_id(self):
        if "card_back_id" in self._data.keys():
            return self._data["card_back_id"]
        else:
            raise LookupError('Card has no value "card_back_id"')
        
    def collector_number(self):
        if "collector_number" in self._data.keys():
            return self._data["collector_number"]
        else:
            raise LookupError('Card has no value "collector_number"')
    
    def content_warning(self):
        if "content_warning" in self._data.keys():
            return self._data["content_warning"]
        else:
            raise LookupError('Card has no value "content_warning"')
    
    def digital(self):
        if "digital" in self._data.keys():
            return self._data["digital"]
        else:
            raise LookupError('Card has no value "digital"')
    
    def finishes(self):
        if "finishes" in self._data.keys():
            return self._data["finishes"]
        else:
            raise LookupError('Card has no value "finishes"')
    
    def flavor_name(self):
        if "flavor_name" in self._data.keys():
            return self._data["flavor_name"]
        else:
            raise LookupError('Card has no value "flavor_name"')
    
    def flavor_text(self):
        if "flavor_text" in self._data.keys():
            return self._data["flavor_text"]
        else:
            raise LookupError('Card has no value "flavor_text"')
    
    def frame_effects(self):
        if "frame_effects" in self._data.keys():
            return self._data["frame_effects"]
        else:
            raise LookupError('Card has no value "frame_effects"')
    
    def frame(self):
        if "frame" in self._data.keys():
            return self._data["frame"]
        else:
            raise LookupError('Card has no value "frame"')
    
    def full_art(self):
        if "full_art" in self._data.keys():
            return self._data["full_art"]
        else:
            raise LookupError('Card has no value "full_art"')
    
    def games(self):
        if "games" in self._data.keys():
            return self._data["games"]
        else:
            raise LookupError('Card has no value "games"')
    
    def highres_image(self):
        if "highres_image" in self._data.keys():
            return self._data["highres_image"]
        else:
            raise LookupError('Card has no value "highres_image"')
    
    def illustration_id(self):
        if "illustration_id" in self._data.keys():
            return self._data["illustration_id"]
        else:
            raise LookupError('Card has no value "illustration_id"')
    
    def image_status(self):
        if "image_status" in self._data.keys():
            return self._data["image_status"]
        else:
            raise LookupError('Card has no value "image_status"')
    
    def image_uris(self):
        if "image_uris" in self._data.keys():
            return self._data["image_uris"]
        else:
            raise LookupError('Card has no value "image_uris"')
    
    def prices(self):
        if "prices" in self._data.keys():
            return self._data["prices"]
        else:
            raise LookupError('Card has no value "prices"')
    
    def printed_name(self):
        if "printed_name" in self._data.keys():
            return self._data["printed_name"]
        else:
            raise LookupError('Card has no value "printed_name"')
    
    def printed_text(self):
        if "printed_text" in self._data.keys():
            return self._data["printed_text"]
        else:
            raise LookupError('Card has no value "printed_text"')
    
    def printed_type_line(self):
        if "printed_type_line" in self._data.keys():
            return self._data["printed_type_line"]
        else:
            raise LookupError('Card has no value "printed_type_line"')
    
    def promo(self):
        if "promo" in self._data.keys():
            return self._data["promo"]
        else:
            raise LookupError('Card has no value "promo"')
    
    def promo_types(self):
        if "promo_types" in self._data.keys():
            return self._data["promo_types"]
        else:
            raise LookupError('Card has no value "promo_types"')
    
    def purchase_uris(self):
        if "purchase_uris" in self._data.keys():
            return self._data["purchase_uris"]
        else:
            raise LookupError('Card has no value "purchase_uris"')
    
    def rarity(self):
        if "rarity" in self._data.keys():
            return self._data["rarity"]
        else:
            raise LookupError('Card has no value "rarity"')
    
    def related_uris(self):
        if "related_uris" in self._data.keys():
            return self._data["related_uris"]
        else:
            raise LookupError('Card has no value "related_uris"')
    
    def released_at(self):
        if "released_at" in self._data.keys():
            return self._data["released_at"]
        else:
            raise LookupError('Card has no value "released_at"')
    
    def reprint(self):
        if "reprint" in self._data.keys():
            return self._data["reprint"]
        else:
            raise LookupError('Card has no value "reprint"')
    
    def scryfall_set_uri(self):
        if "scryfall_set_uri" in self._data.keys():
            return self._data["scryfall_set_uri"]
        else:
            raise LookupError('Card has no value "scryfall_set_uri"')
        
    def set_name(self):
        if "set_name" in self._data.keys():
            return self._data["set_name"]
        else:
            raise LookupError('Card has no value "set_name"')

    def set_search_uri(self):
        if "set_search_uri" in self._data.keys():
            return self._data["set_search_uri"]
        else:
            raise LookupError('Card has no value "set_search_uri"')
    
    def set_type(self):
        if "set_type" in self._data.keys():
            return self._data["set_type"]
        else:
            raise LookupError('Card has no value "set_type"')
    
    def set_uri(self):
        if "set_uri" in self._data.keys():
            return self._data["set_uri"]
        else:
            raise LookupError('Card has no value "set_uri"')
    
    def set_code(self):
        if "set" in self._data.keys():
            return self._data["set"]
        else:
            raise LookupError('Card has no value "set_code"')
    
    def set_id(self):
        if "set_id" in self._data.keys():
            return self._data["set_id"]
        else:
            raise LookupError('Card has no value "set_id"')
    
    def story_spotlight(self):
        if "story_spotlight" in self._data.keys():
            return self._data["story_spotlight"]
        else:
            raise LookupError('Card has no value "story_spotlight"')
    
    def textless(self):
        if "textless" in self._data.keys():
            return self._data["textless"]
        else:
            raise LookupError('Card has no value "textless"')
    
    def variation(self):
        if "variation" in self._data.keys():
            return self._data["variation"]
        else:
            raise LookupError('Card has no value "variation"')
    
    def variation_of(self):
        if "variation_of" in self._data.keys():
            return self._data["variation_of"]
        else:
            raise LookupError('Card has no value "variation_of"')
    
    def security_stamp(self):
        if "security_stamp" in self._data.keys():
            return self._data["security_stamp"]
        else:
            raise LookupError('Card has no value "security_stamp"')
    
    def watermark(self):
        if "watermark" in self._data.keys():
            return self._data["watermark"]
        else:
            raise LookupError('Card has no value "watermark"')
    
    def preview_previewed_at(self):
        if "preview_previewed_at" in self._data.keys():
            return self._data["preview_previewed_at"]
        else:
            raise LookupError('Card has no value "preview_previewed_at"')
    
    def preview_source_uri(self):
        if "preview_source_uri" in self._data.keys():
            return self._data["preview_source_uri"]
        else:
            raise LookupError('Card has no value "preview_source_uri"')
    
    def preview_source(self):
        if "preview_source" in self._data.keys():
            return self._data["preview_source"]
        else:
            raise LookupError('Card has no value "preview_source"')



        
    def __str__(self):
        return f"{self.name()} ({self.set_code()})"

    def __repr__(self):
        return f"{self.name()} ({self.set_code()})"

    def __eq__(self, other):
        return self._data['name'] == other.data()['name']