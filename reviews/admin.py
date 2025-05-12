from django.contrib import admin
from .models import Movie, Review
from django.db.models import Count, Avg, F, Q

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'average_rating_display', 'review_count_display')

    def average_rating_display(self, obj):
        return obj.average_rating()
    average_rating_display.short_description = 'Note moyenne'

    def review_count_display(self, obj):
        return obj.review_count()
    review_count_display.short_description = 'Nombre d’avis'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'predicted_rating', 'user_rating', 'is_modified', 'created_at')
    list_filter = ('movie', 'created_at')

    change_list_template = "admin/reviews/review_changelist.html"  

    def changelist_view(self, request, extra_context=None):
        stats = Review.objects.aggregate(
            total_reviews=Count('id'),
            unchanged_count=Count('id', filter=Q(predicted_rating=F('user_rating'))),
            avg_diff=Avg(F('predicted_rating') - F('user_rating'))
        )
        extra_context = extra_context or {}
        extra_context['stats'] = stats
        return super().changelist_view(request, extra_context=extra_context)
