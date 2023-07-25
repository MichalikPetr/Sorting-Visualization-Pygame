import pygame
import random

class SortingList:
    def __init__(self, window, size, space):
        self.values = list(range(1, size + 1))
        self.colors = dict.fromkeys(self.values, "gray")
        self.size = size
        self.space = space
        self.window = window

    def draw(self):
        start = self.space[0]
        end = self.space[0] + self.space[2]
        top = self.space[1]
        bottom = self.space[1] + self.space[3]

        item_width = (end - start) / (self.size * 2 - 1)
        item_height = (bottom - top) / self.size

        pygame.draw.rect(self.window, "black", self.space)
        for index, number in enumerate(self.values):
            pygame.draw.rect(self.window, self.colors[number], [start + index * 2 * item_width,
                                                    bottom - item_height * number,
                                                    item_width,
                                                    item_height * number])
        
        pygame.display.update(self.space)
        pygame.event.pump()
            
    def shuffle(self):
        random.shuffle(self.values)

    def sort(self, algorithm):
        if algorithm == "bubblesort":
            self.bubblesort()    

        elif algorithm == "quicksort":
            self.quicksort(0, self.size - 1)

        elif algorithm == "selectsort":
            self.selectsort()    


    #algorithms 
    def selectsort(self):
        for i in range(self.size):
            min_i = i

            for j in range(i + 1, self.size):
                if self.values[j] < self.values[min_i]:
                    min_i = j

            self.colors[self.values[min_i]] = "red"
            self.draw()
            self.colors[self.values[min_i]] = "gray"

            self.values[i], self.values[min_i] = self.values[min_i], self.values[i]

    def bubblesort(self):
        for i in range(self.size - 1):
            for j in range(0, self.size - i - 1):
                self.colors[self.values[j]] = "red"
                self.draw()
                self.colors[self.values[j]] = "gray"

                if self.values[j] > self.values[j + 1]:
                    self.values[j], self.values[j + 1] = self.values[j + 1], self.values[j]

    def partition(self, start, end):
        pivot = self.values[end]        #select last element as pivot
        self.colors[pivot] = "green"

        i = start - 1                   #index of elements higher, than pivot

        for j in range(start, end):
            self.colors[self.values[j]] = "red"
            self.draw()
            self.colors[self.values[j]] = "gray"    

            if self.values[j] <= pivot:         #if element is higher, put it before pivot
                i += 1
                self.values[i], self.values[j] = self.values[j], self.values[i]

        self.values[i + 1], self.values[end] = self.values[end], self.values[i + 1]     #put pivot to its place

        self.colors[pivot] = "gray"
        return i + 1                            #return index of pivot


    def quicksort(self, start, end):
        if start < end:
            pivot_index = self.partition(start, end)

            self.quicksort(start, pivot_index - 1)
            self.quicksort(pivot_index + 1, end)

        