from torch.autograd import Variable

#image = torch.unsqueeze(image,0)

image_copy = np.copy(image)

roi_arr = []
roi_output = []

for (x,y,w,h) in faces:
   
    # Select the region of interest that is the face in the image 
    roi = image_copy[y:y+h, x:x+w]
    roi_arr.append(roi)
    ## TODO: Convert the face region from RGB to grayscale
    roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
    ## TODO: Normalize the grayscale image so that its color range falls in [0,1] instead of [0,255]
    roi = roi / 255
    ## TODO: Rescale the detected face to be the expected square size for your CNN (224x224, suggested)
    roi = cv2.resize(roi, (224, 224))
    ## TODO: Reshape the numpy image shape (H x W x C) into a torch image shape (C x H x W)
    
    #FEEDBACK FROM REVIEWER
    if len(roi.shape) == 2:
        roi = np.expand_dims(roi, axis=0)
    else:
        roi = np.rollaxis(roi, 2, 0)
        
    ## TODO: Make facial keypoint predictions using your loaded, trained network 
    roi = np.expand_dims(roi, axis=0)
    roi = Variable(FloatTensor(roi))
    output_pts = net.forward(roi)
    #more needs to be done to the outputs?
    
    output_pts = output_pts.data.numpy()[0]
    output_pts = output_pts.reshape(68, 2)
    
    roi_output.append(output_pts)