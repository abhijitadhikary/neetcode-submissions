class DynamicArray {
private:
    int *arr;
    int size = 0;
    int capacity = 0;
public:

    DynamicArray(int capacity) {
        arr = new int[capacity];
        size = 0;
        this->capacity = capacity;
    }

    int get(int i) {
        if ((i < size) && (i >= 0)) return arr[i];
        return -1;
    }

    void set(int i, int n) {
        if (i >= 0) {
            if (i < size) {
                arr[i] = n;
                // size++;
            } else if (i == size) {
                if (i == capacity) resize();
                arr[i] = n;
                size++;
            }
        }
        
    }

    void pushback(int n) {
        if (size == capacity) resize();
        set(size, n);

    }

    int popback() {
        size--;
        return arr[size];

    }

    void resize() {
        int newCapacity = int(capacity * 2);
        int *tempArray = new int[newCapacity];

        for (int index=0; index<size; index++) {
            tempArray[index] = arr[index];
        }

        delete arr;

        arr = tempArray;
        capacity = newCapacity;

        
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
