def login_logout(test):
    """Connecte l'utilisateur, effectue le test puis le déconnecte

    :param test: La fonction effectuant le test
    :type test: function
    :return: La effectuant le test entouré des instruction de connecxion est de déconnection
    :rtype: function
    """

    def login_logout_decorator(*param, **param2):
        self = param[0]
        self.client.login(username=self.user.username, password=self.password)
        test(*param, **param2)
        self.client.logout()

    return login_logout_decorator
