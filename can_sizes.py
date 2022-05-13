"""
MTristan 
12/05/2022
"""

import math

def main():
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#1 Picnic {storage_efficiency:.2f}")
    radius = 7.78
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#1 Tall {storage_efficiency:.2f}")
    radius = 8.73
    height = 11.59
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#2 {storage_efficiency:.2f}")
    radius = 10.32
    height = 11.91
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#2.5 {storage_efficiency:.2f}")
    radius = 10.79
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#3 Cylinder {storage_efficiency:.2f}")
    radius = 13.02
    height = 14.29
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#5 {storage_efficiency:.2f}")
    radius = 5.40
    height = 8.89
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#6Z {storage_efficiency:.2f}")
    radius = 6.83
    height = 7.62
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#8Z short {storage_efficiency:.2f}")
    radius = 15.72
    height = 17.78
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#10 {storage_efficiency:.2f}")
    radius = 6.83
    height = 12.38
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#211 {storage_efficiency:.2f}")
    radius = 7.62
    height = 11.27
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#300 {storage_efficiency:.2f}")
    radius = 8.10
    height = 11.11
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"#303 {storage_efficiency:.2f}")

def compute_volume(radius, height):
    volume = math.pi *( radius**2) * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()