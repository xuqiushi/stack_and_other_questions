if __name__ == "__main__":
    liste1 = ["Jean", "Maximilien", "Brigitte", "Sonia", "Jean-Pierre", "Sandra"]

    moins6 = []
    plus6 = []
    i = 0
    for name in liste1:
        if len(liste1[i]) > 6:
            moins6.append(liste1[i])
        else:
            plus6.append(liste1[i])
