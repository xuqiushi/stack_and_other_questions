if __name__ == "__main__":
    my_device_list = ['Iphone', 'Samsung', 'Nokia', 'MI']
    deviceString = 'Device_ID='
    combined__device_list = []
    final_combined_list = []
    for x in my_device_list:
        combined__device_list.append(deviceString + "\"" + x + "\"")
    print(' OR '.join(e for e in combined__device_list))