#!/usr/bin/env python3
from 4-task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

print("\nMethod Resolution Order (MRO):")
print(FlyingFish.mro())
