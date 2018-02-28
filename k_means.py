from random import randint

def k_means(data, K):
    """
    k-Means clustering

    TODO: Assumes values from 0-255

    :param data: NxD array of numbers
    :param K: The number of clusters
    :return: Tuple of cluster means (KxD array) and cluster assignments (Nx1 with values from 1 to K)
    """

    N = len(data)
    D = len(data[0])

    means = [None]*K
    for i in range(0,K):
        means[i] = [randint(0, 255), randint(0, 255), randint(0, 255)]

    assignments = [None]*N

    changed = True
    while(changed):
        old_means = means

        # Find closest centroid
        for n in range(0, N):
            "max distance in RGB"
            min = 442.0
            index = -1
            for k in range(0,K):
                temp = __distance(data[n], means[k], D)
                if temp <= min:
                    min = temp
                    index = k

            assignments[n] = index

        # Calculate the new centers
        for k in range(0,K):
            # Aus assignments die Indizes mit Eintrag k finden
            indices = [i for i,x in enumerate(assignments) if x == k]
            # ... und dann anhand derer in Data die Werte schauen
            temp_data = [x for i,x in enumerate(data) if i in indices]
            # ... und mitteln
            means[k] = __mean(temp_data, D)

        # Check if something changed
        changed = False
        for k in range(0,K):
            if old_means[k] != means[k]:
                changed = True
                break

    return (means, assignments)

def __distance(a, b, dim):
    sum = 0.0
    for i in range(0,dim):
        sum += (a[i]-b[i])**2
    return sum**(1/2.0)

def __mean(a, dim):
    N = len(a)
    sum = [0.0]*dim
    for e in a:
        for d in range(0,dim):
            sum[d] += e[d]
    avg = [a/N for a in sum]
    return avg
