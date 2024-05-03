from models.text_summary_model import TextSummary


class TruncateTestData:
    def truncate_test_summarie_data(self):
        summaries = TextSummary.all().delete()
        if not summaries:
            return {"message": "Your database model not exists summarie data"}
        return {"message": "All summarie deleted successfully"}
