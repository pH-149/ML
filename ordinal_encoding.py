from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
import numpy as np

# Sample categorical data for ordinal encoding
data = np.array([
    ['Low'],
    ['Medium'],
    ['High'],
    ['Medium'],
    ['Low'],
    ['High']
])

# Initialize the ordinal encoder
ordinal_encoder = OrdinalEncoder()

# Fit and transform the data using ordinal encoding
ordinal_encoded_data = ordinal_encoder.fit_transform(data)

print("Original Data:")
print(data)
print("\nOrdinal Encoded Data:")
print(ordinal_encoded_data)

# Sample categorical data for label encoding
labels = ['cat', 'dog', 'fish', 'dog', 'cat', 'fish']

# Initialize the label encoder
label_encoder = LabelEncoder()

# Fit and transform the labels using label encoding
label_encoded_data = label_encoder.fit_transform(labels)

print("\nOriginal Labels:")
print(labels)
print("\nLabel Encoded Data:")
print(label_encoded_data)
