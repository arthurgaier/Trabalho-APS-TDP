def main():
    plt.figure(figsize=(10,6))
    plt.plot(data_df["Constante"],data_df["Tempo iterativo (s)"],label = "Função iterativa",color = "r")
    plt.plot(data_df["Constante"],data_df["Tempo Recursivo (s)"],label = "Função recursiva",color = "b")
    plt.title("Quicksort em funções diferentes")
    plt.xlabel("Quantidade de elementos")
    plt.ylabel("Tempo (s)")
    plt.xticks([0,5000,15000,50000,100000])
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()