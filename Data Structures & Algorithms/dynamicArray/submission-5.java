class DynamicArray {
    private int lastIndex;
    private int capacity;
    private int[] array;

    public DynamicArray(int capacity) {
        this.lastIndex = -1;
        this.capacity = capacity;
        this.array = new int[capacity];
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (lastIndex + 1 >= capacity) resize();

        this.lastIndex++;
        this.array[lastIndex] = n;
    }

    public int popback() {
        int lastItem = this.array[lastIndex];

        this.lastIndex--;

        return lastItem;
    }

    private void resize() {
        var newArray = new int[this.capacity * 2];
        
        for (int i = 0; i < this.array.length; i++) {
            newArray[i] = this.array[i];
        }

        this.array = newArray;
        this.capacity *= 2;
    }

    public int getSize() {
        return lastIndex + 1;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
