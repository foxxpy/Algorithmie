def string_is_palindrome(string):
    """Test si une chaîne de caractères est un palindrome"""
    
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return string_is_palindrome(string[1:-1])
        else:
            return False
