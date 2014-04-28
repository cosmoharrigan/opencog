ADD_LIBRARY(behavior SHARED
    BDTracker
    BE
    PAIWorldProvider
    BasicWorldProvider
    PredicateHandleSet
    BehaviorCategory
    BehaviorDescriptionMatcher
    CompositeBehaviorDescription
    EvaluationLinkSimilarityEvaluator
    BDRetriever
)

TARGET_LINK_LIBRARIES (behavior
	PAI
	AtomSpaceExtensions
	atomspace
	cogutil
)
