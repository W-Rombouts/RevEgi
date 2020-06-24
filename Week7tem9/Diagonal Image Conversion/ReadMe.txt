This codes uses an offset when there is a diagonal split in the image where as the left part of the images goes to the right.
Why: A minor in Reversed Engineering once had a task to capture easter eggs and I could not handle a weird image in my documentation.

Example Image has a size of 415x300 and has a offset correction starting at 116 adding +1 for each row

Library:
- pillow

The code is built using a rebuild_image_offset and create_image_from_rgb_list function:
FUNCTION: rebuild_image_offset
  Parameters (location of the image, save name and location, offset for splitting the row, image pixel width)
  1. Opens the original images 
  2. Creates a list using Pillow.getdata() to receive the colors from each pixel
  3. Splits the list into the rows (slice after each pixel == max_width)
  4. Determines the split location based on the offset
  5. Add the SECOND part of the row to the new pixel list
  6. Add the First part of the row to the new pixel list
  7. Call function create_image_from_rgb_list
  
FUNCTION: create_image_from_rgb_list
  Parameters (image object from function rebuild_image_offset, list of new pixels, save name and location)
  1. Create a new Image.new with the image object
  2. Convert the array into a tuple and list
  3. Create and save the image
  
  
#TODO: Create a function that gets the pixel width of the image by itself
