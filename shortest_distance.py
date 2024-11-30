import networkx as nx
import matplotlib.pyplot as plt

# ایجاد گراف جهت‌دار
G = nx.DiGraph()

# اضافه کردن راس‌ها
for i in range(1, 13):
    G.add_node(i)

# اضافه کردن یال‌ها با وزن (تعداد یال‌ها بیشتر شده است)
G.add_weighted_edges_from([
    (1, 2, 4),
    (1, 3, 2),
    (1, 4, 7),
    (2, 4, 5),
    (2, 5, 3),
    (3, 2, 1),
    (3, 4, 8),
    (3, 6, 6),
    (4, 5, 3),
    (4, 6, 1),
    (5, 6, 2),
    (5, 7, 4),
    (6, 8, 7),
    (7, 8, 5),
    (7, 9, 4),
    (8, 10, 6),
    (9, 10, 3),
    (9, 11, 2),
    (10, 11, 5),
    (11, 12, 3),
    (12, 1, 6),
    (12, 9, 1),
    (1, 7, 6),
    (3, 12, 8),
    (6, 11, 2)
])

# دریافت دو راس از کاربر
start_node = int(input("رأس مبدأ را وارد کنید: "))
end_node = int(input("رأس مقصد را وارد کنید: "))

# محاسبه کوتاه‌ترین مسیر با استفاده از الگوریتم دیکسترا
shortest_path = nx.dijkstra_path(G, start_node, end_node)
shortest_distance = nx.dijkstra_path_length(G, start_node, end_node)

# نمایش نتیجه
print(f"کوتاه‌ترین مسیر از رأس {start_node} به رأس {end_node}: {shortest_path}")
print(f"مسافت کوتاه‌ترین مسیر: {shortest_distance}")

# رسم گراف
pos = nx.spring_layout(G)  # تعیین موقعیت راس‌ها برای رسم
plt.figure(figsize=(12, 10))
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20)

# نمایش یال‌ها با وزن
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

# هایلایت کردن مسیر کوتاه‌ترین
edges_in_path = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="red", width=2)

# نمایش گراف
plt.title("گراف جهت‌دار با یال‌های بیشتر و کوتاه‌ترین مسیر")
plt.show()