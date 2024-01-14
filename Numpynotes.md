# Funkcje NumPy

## Tworzenie
- `np.arange([start, ], stop, [step, ], dtype=None)` – Zwraca tablicę wartości w danym przedziale.
- `np.random.rand(d0, d1, …, dn)` – Tworzy tablicę o danych wymiarach z losowymi wartościami.
- `np.array(arr, dtype=typ)` - Tworzy tablicę numpy.

## Właściwości Tablicy
- `x.ndim` – Liczba wymiarów tablicy.
- `x.shape` – Wymiary tablicy.
- `x.dtype` – Typ danych elementów tablicy.

## Przekształcenia Tablicy
- `np.reshape(a, newshape, order='C')` – Zmienia kształt tablicy bez zmiany danych.
- `A[x:y]` – Wycinanie wierszy, `A[:, x:y]` – Wycinanie kolumn.
- `np.resize(a, new_shape)` – Zwraca tablicę o określonym kształcie.
- `np.transpose(A)` – Transpozycja macierzy.
- `A.reshape(-1)` – Zmiana na 1D.

## Wstawianie i Usuwanie
- `numpy.insert(arr, obj, values, axis=None)` – Wstawia wartości na określony indeks.
- `numpy.append(arr, values, axis=None)` – Dodaje wartości na końcu tablicy.
- `numpy.delete(arr, obj, axis=None)` – Usuwa wybrane elementy.

## Operacje Arytmetyczne
- `np.dot, @` – Iloczyn skalarny, mnożenie macierzy.
- `*` – Mnożenie element przez element.
- `np.power, **` – Potęgowanie.
- `np.power(x1, ex)` – Podnosi do potęgi.

## Funkcje Agregujące
- `np.sum(a, axis=None)` – Suma elementów tablicy.
- `np.prod(x)` – Iloczyn wszystkich elementów.
- `np.cumprod(x)` – Skumulowany iloczyn [1,2,3,4] → [1, 2, 6, 24].
- `np.mean(x)` - Średnia.
- `np.median(x)` – Mediana.
- `np.std(x)` – Odchylenie standardowe.
- `np.var(x)` – Wariancja.

## Funkcje Statystyczne i Poszukiwania
- `np.max(a, axis=None), np.min(a, axis=None)` – Maksymalna i minimalna wartość w tablicy.
- `np.argmax(A), np.argmin(A)` – Indeks największego/najmniejszego elementu.
- `np.argmax(A, axis=0), np.argmin(A, axis=0)` – Indeksy największych/najmniejszych elementów w kolumnach.
- `np.argmax(A, axis=1), np.argmin(A, axis=1)` – Indeksy największych/najmniejszych elementów w wierszach.
- `np.argsort(x)`  - Sortowanie po argumentach.

## Algebra Liniowa
- `np.linalg.inv(A)` – Macierz odwrotna do `A`.
- `np.linalg.det(A)` – Wyznacznik macierzy `A`.
- `np.trace(A)` – Suma elementów na przekątnej macierzy.
- `np.linalg.norm(A)` – Norma Euklidesowa macierzy.
- `np.linalg.solve(a, b)` – Rozwiązuje układ równań liniowych.
- `np.linalg.qr(A)` – Rozkład QR macierzy.
- `np.linalg.svd(A)` – Rozkład według wartości osobliwych (SVD) macierzy.

## Dodatkowe Funkcje
- `np.clip(a, a_min, a_max)` – Ogranicza wartości w tablicy do określonego zakresu.
- `np.sqrt(x)` – Pierwiastek kwadratowy każdego elementu tablicy.
- `np.abs(x)` – Wartość bezwzględna każdego elementu tablicy.
- `np.invert(a)` – Odwraca wartości logiczne (NOT) dla tablicy typu bool.
- `np.count_nonzero(a)` – Liczy niezerowe elementy tablicy.
- `np.unique(a)` – Zwraca posortowane unikalne elementy tablicy.
- `np.all(), np.any()` - Sprawdza, czy wszystkie/przynajmniej jeden element tablicy są prawdziwe.
- `np.concatenate((x, y), axis=0), np.concatenate((x, y), axis=1)` - Łączenie tablic wierszowo/kolumnowo.
- `np.split(x, n)` - Podział tablicy na `n` podtablic.
