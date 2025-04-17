# SPDX-License-Identifier: Apache-2.0

from vllm.model_executor.parameter import (BasevLLMParameter,
                                           PackedvLLMParameter)
from vllm.model_executor.sampling_metadata import (SamplingMetadata,
                                                   SamplingMetadataCache)
from vllm.model_executor.utils import set_random_seed

__all__ = [
    "SamplingMetadata",
    "SamplingMetadataCache",
    "set_random_seed",
    "BasevLLMParameter",
    "PackedvLLMParameter",
]

NEW_TOKENS = [f"[REVIEW_TOKEN_{i}]" for i in range(8)]
NEW_TOKEN_IDS = [
    151665,
    151666,
    151667,
    151668,
    151669,
    151670,
    151671,
    151672,
]
