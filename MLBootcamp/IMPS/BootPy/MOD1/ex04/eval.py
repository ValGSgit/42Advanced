
class Evaluator:
    """
    A static method is a method that does not receive self or cls automatically. 
    It behaves like a normal function but is placed inside a class because it logically belongs there. 
    It cannot access or modify class or instance data directly.
    The 'weight' is the length of each word
    """
    @staticmethod
    def zip_evaluate(coefs, words):
        """Compute sum of lengths of every word in lst weighted by a list of coefficients"""
        for word in words:
            if not isinstance(word, str):
                raise Exception("Words list has a no word element\n")
        for num in coefs:
            if not isinstance(num, (float, int)):
                raise Exception("Coefficients has a not (float, int) element\n")
        if not len(words) == len(coefs):
            return -1
        count = 0
        for coef, word in zip(coefs, words):
            count += coef * len(word)
        return count
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        """Compute count of lengths of every word in lst weighted by a list of coefficients"""
        for word in words:
            if not isinstance(word, str):
                raise Exception("Words list has a no word element\n")
        for num in coefs:
            if not isinstance(num, (float, int)):
                raise Exception("Coefficients has a not (float, int) element\n")
        if not len(words) == len(coefs):
            return -1
        count = 0
        for i, word in enumerate(words, 0):
            count += coefs[i] * len(word)
        return count


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))