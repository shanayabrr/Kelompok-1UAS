import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, kota):
        if kota not in self.graph:
            self.graph[kota] = {}

    def tambah_jalan(self, kota1, kota2, jarak):
        self.tambah_kota(kota1)
        self.tambah_kota(kota2)
        self.graph[kota1][kota2] = jarak
        self.graph[kota2][kota1] = jarak  # Karena graph ini tidak berarah

    def dijkstra(self, awal, tujuan):
        jarak = {kota: float('inf') for kota in self.graph}
        jarak[awal] = 0
        pq = [(0, awal)]  # Priority Queue (heap)
        jalur = {}

        while pq:
            jarak_sementara, kota_sekarang = heapq.heappop(pq)

            if kota_sekarang == tujuan:
                break

            for tetangga, bobot in self.graph[kota_sekarang].items():
                jarak_baru = jarak_sementara + bobot

                if jarak_baru < jarak[tetangga]:
                    jarak[tetangga] = jarak_baru
                    heapq.heappush(pq, (jarak_baru, tetangga))
                    jalur[tetangga] = kota_sekarang

        path, kota = [], tujuan
        while kota in jalur:
            path.insert(0, kota)
            kota = jalur[kota]
        path.insert(0, awal)

        return path, jarak[tujuan]

peta = Graph()
peta.tambah_jalan("tajur", "bubulak", 5)
peta.tambah_jalan("tajur", "sempur", 2)
peta.tambah_jalan("bubulak", "laladon", 8)
peta.tambah_jalan("sempur", "laladon", 3)
peta.tambah_jalan("bubulak", "sempur", 1)

awal = str(input("Pilih kota tajur, bubulak, sempur, laladon:"))
tujuan = str(input("Pilih kota tajur, bubulak, sempur, laladon:"))
jalur_terpendek, jarak_total = peta.dijkstra(awal, tujuan)

print(f"Jalur tercepat dari {awal} ke {tujuan}: {' -> '.join(jalur_terpendek)}")
print(f"Total jarak: {jarak_total} km")

