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

NEW_TOKENS = [f"[HIS_TOKEN_{i}]" for i in range(64)] + ["[INST_TOKEN]"]
NEW_TOKEN_IDS = [
    151665, 151666, 151667, 151668, 151669, 151670, 151671, 151672, 151673,
    151674, 151675, 151676, 151677, 151678, 151679, 151680, 151681, 151682,
    151683, 151684, 151685, 151686, 151687, 151688, 151689, 151690, 151691,
    151692, 151693, 151694, 151695, 151696, 151697, 151698, 151699, 151700,
    151701, 151702, 151703, 151704, 151705, 151706, 151707, 151708, 151709,
    151710, 151711, 151712, 151713, 151714, 151715, 151716, 151717, 151718,
    151719, 151720, 151721, 151722, 151723, 151724, 151725, 151726, 151727,
    151728, 151729
]
