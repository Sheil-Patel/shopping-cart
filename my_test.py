from shopping_cart import to_usd

def test_to_usd():
    result = to_usd(3.50)
    assert result == "$3.50"


    #assert determine_winner("rock","rock") == None
    #assert determine_winner("rock" , "paper") == "paper"