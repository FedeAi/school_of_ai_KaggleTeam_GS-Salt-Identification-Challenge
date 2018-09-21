import tensorflow as tf
import keras.backend as K

def precision(y_true, y_pred):
    """Calculate mean precision for batch of images"""
    y_true_ = tf.cast(tf.round(y_true), dtype=tf.float32)
    y_pred_ = tf.cast(tf.round(y_pred), dtype=tf.float32)
    
    #Flatten the prediction and the target
    y_true_ = tf.reshape(y_true_, shape=[tf.shape(y_pred_)[0], -1])    
    y_pred_ = tf.reshape(y_pred_, shape=[tf.shape(y_pred_)[0], -1])
    
    #Intersection over union threshold 
    threasholds_iou = tf.constant(np.arange(0.5, 1.0, 0.05), dtype=tf.float32)
    
    #Add the prediction and the mask toguether
    total = tf.cast(y_true_ + y_pred_, dtype = tf.int32)
        
    #Where total == 2
    intersection = tf.reduce_sum(tf.cast(tf.greater(total, 1), tf.float32), axis = 1)
        
    #Where total == 2 | total == 1
    union = tf.reduce_sum(tf.cast(tf.greater(total, 0) , tf.float32), axis = 1)
        
    #Intersection over union
    iou = tf.divide(intersection, union)
        
    #Change NaNs to 1 because they represent true negatives
    iou = tf.where(tf.is_nan(iou), tf.ones_like(iou), iou)
        
    #Compare IoU to thresholds
    iou = K.repeat_elements(tf.reshape(iou, shape = [tf.shape(iou)[0],1]),10, axis = 1)
    
    #Calculate score for each image
    greater = tf.greater(iou, threasholds_iou)
    scores = tf.reduce_mean(tf.cast(greater, tf.float32), axis = 1)

    #Average score for batch of images
    return tf.reduce_mean(scores)
