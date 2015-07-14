# The idea is to open the file, go through each line, add the camera to a list only if the list doesn't already contain the camera. Once that's complete, we create a new file, and add each camera from the list to this newly created file.

f = open(“camera_list.txt”, “r”)
cameras = []
for line in f.readlines():
	if line not in cameras:
		cameras.append(line)
f.close()
f1 = open (“new_camera_list.txt”, “w”)
for camera in cameras:
	f1.write(camera + “\n")
f1.close()
