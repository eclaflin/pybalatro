class Card:

    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    # Dictionary of the face and it's attributes
    FACES = {
        'A': {
            "face_name":"Ace",
            "is_face":False, 
            "numeric_val":1
            }, 
        '2': {
            "face_name":"Two",
            "is_face":False, 
            "numeric_val":2
            }, 
        '3': {
            "face_name":"Three",
            "is_face":False, 
            "numeric_val":3
            }, 
        '4': {
            "face_name":"Four",
            "is_face":False, 
            "numeric_val":4
            }, 
        '5': {
            "face_name":"Five",
            "is_face":False, 
            "numeric_val":5
            }, 
        '6': {
            "face_name":"Six",
            "is_face":False, 
            "numeric_val":6
            }, 
        '7': {
            "face_name":"Seven",
            "is_face":False, 
            "numeric_val":7
            }, 
        '8': {
            "face_name":"Eight",
            "is_face":False, 
            "numeric_val":8
            }, 
        '9': {
            "face_name":"Nine",
            "is_face":False, 
            "numeric_val":9
            }, 
        '10': {
            "face_name":"Ten",
            "is_face":False, 
            "numeric_val":10
            }, 
        'J': {
            "face_name":"Jack",
            "is_face":True, 
            "numeric_val":10
            }, 
        'Q': {
            "face_name":"Queen",
            "is_face":True, 
            "numeric_val":10
            }, 
        'K': {
            "face_name":"King",
            "is_face":True,
            "numeric_val":10
            }, 
    }


    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.face_name = Card.FACES[self.face]['face_name']
        self.is_face = Card.FACES[self.face]["is_face"]
        self.numeric_val = Card.FACES[self.face]["numeric_val"]


    def __repr__(self):
        return f"Card(suit='{self.suit}', face_name='{self.face_name}', is_face='{self.is_face}', numeric_val='{self.numeric_val}')"
