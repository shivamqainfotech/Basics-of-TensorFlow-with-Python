package com.qait.svm.TF;

import java.nio.file.Paths;
import java.util.List;

import org.tensorflow.Tensor;
import org.tensorflow.TensorFlow;

public class LabelImage_Main {

	private static final String modelDir = "D:\\TrafficSigns";
	private static final String imageFile = "D:\\TrafficSigns\\images\\dam.jpg";

	public static void main(String[] args) {

		System.out.println("TensorFlow version: " + TensorFlow.version());

		byte[] graphDef = LabelImage.readAllBytesOrExit(Paths.get(modelDir, "tensorflow_inception_graph.pb"));
		List<String> labels = LabelImage
				.readAllLinesOrExit(Paths.get(modelDir, "imagenet_comp_graph_label_strings.txt"));
		byte[] imageBytes = LabelImage.readAllBytesOrExit(Paths.get(imageFile));

		try (Tensor image = LabelImage.constructAndExecuteGraphToNormalizeImage(imageBytes)) {
			float[] labelProbabilities = LabelImage.executeInceptionGraph(graphDef, image);
			int bestLabelIdx = LabelImage.maxIndex(labelProbabilities);
			System.out.println(String.format("BEST MATCH: %s (%.2f%% likely)", labels.get(bestLabelIdx),
					labelProbabilities[bestLabelIdx] * 100f));
		}
	}
}
