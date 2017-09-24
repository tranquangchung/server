import librosa
import numpy
# from sklearn.cluster import KMeans


class LowLevelMusic():
    def __init__(self, name):
        self.name = name
        self.fs = 44100
        self.frame_sz = 4410

    def extract_features(self):
        x, sr = librosa.load(self.name)
        onset_frames = librosa.onset.onset_detect(x, sr=sr)
        features1 = numpy.array([self.extract_features_chroma_stft(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features2 = numpy.array([self.extract_features_chroma_cqt(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features3 = numpy.array([self.extract_features_chroma_cens(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features4 = numpy.array([self.extract_features_melspectrogram(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features5 = numpy.array([self.extract_features_mfcc(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features6 = numpy.array([self.extract_features_rmse(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features7 = numpy.array([self.extract_features_spectral_centroid(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features8 = numpy.array([self.extract_features_spectral_bandwidth(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features9 = numpy.array([self.extract_features_spectral_contrast(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features10 = numpy.array([self.extract_features_spectral_rolloff(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features11 = numpy.array([self.extract_features_poly_features(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features12 = numpy.array([self.extract_features_tonnetz(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        features13 = numpy.array([self.extract_features_zero_crossing_rate(x[i:i + self.frame_sz], self.fs) for i in onset_frames])

        #caculate mean of all feature
        return numpy.array([numpy.mean(features1),
                            numpy.mean(features2),
                            numpy.mean(features3),
                            numpy.mean(features4),
                            numpy.mean(features5),
                            numpy.mean(features6),
                            numpy.mean(features7),
                            numpy.mean(features8),
                            numpy.mean(features9),
                            numpy.mean(features10),
                            numpy.mean(features11),
                            numpy.mean(features12),
                            numpy.mean(features13)
                            ])

    def extract_features_chroma_stft(self, x, fs):
        feature = librosa.feature.chroma_stft(x).sum() # placeholder
        return feature

    def extract_features_chroma_cqt(self, x, fs):
        feature = librosa.feature.chroma_cqt(x).sum() # placeholder
        return feature

    def extract_features_chroma_cens(self, x, fs):
        feature = librosa.feature.chroma_cens(x).sum() # placeholder
        return feature

    def extract_features_melspectrogram(self, x, fs):
        feature = librosa.feature.melspectrogram(x).sum() # placeholder
        return feature

    def extract_features_mfcc(self, x, fs):
        feature = librosa.feature.mfcc(x).sum() # placeholder
        return feature

    def extract_features_rmse(self, x, fs):
        feature = librosa.feature.rmse(x).sum() # placeholder
        return feature

    def extract_features_spectral_centroid(self, x, fs):
        feature = librosa.feature.spectral_centroid(x).sum() # placeholder
        return feature

    def extract_features_spectral_bandwidth(self, x, fs):
        feature = librosa.feature.spectral_bandwidth(x).sum() # placeholder
        return feature

    def extract_features_spectral_contrast(self, x, fs):
        feature = librosa.feature.spectral_contrast(x).sum() # placeholder
        return feature

    def extract_features_spectral_rolloff(self, x, fs):
        feature = librosa.feature.spectral_rolloff(x).sum() # placeholder
        return feature

    def extract_features_poly_features(self, x, fs):
        feature = librosa.feature.poly_features(x).sum() # placeholder
        return feature

    def extract_features_tonnetz(self, x, fs):
        feature = librosa.feature.tonnetz(x).sum() # placeholder
        return feature

    def extract_features_zero_crossing_rate(self, x, fs):
        feature = librosa.feature.zero_crossing_rate(x).sum() # placeholder
        return feature