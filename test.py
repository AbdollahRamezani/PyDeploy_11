from deepface import DeepFace


objs = DeepFace.analyze(
  img_path = "02.jpg", 
  actions = ['age'],
)

print(objs)
