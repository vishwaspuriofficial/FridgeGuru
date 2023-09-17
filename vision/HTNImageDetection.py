
def imageDetection(upload):
    from ultralytics import YOLO
    model = YOLO('vision/FoodModel.pt')
    #try:
    results = model(source=upload, show=True, conf=0.4, save=True)

    if len(results) > 0:
            # Access the first element of the list
            first_result = results[0]

            res = {}
            for i in first_result.boxes.cls:
                class_name = first_result.names[i.item()].replace(".", "")
                if class_name in res:
                    res[class_name] += 1
                else:
                    res[class_name] = 1
    else:
            print("No results found.")
    #except Exception as e:
    #print("her problem")
    return str(res)

if __name__ == '__main__':
    imageDetection(upload)